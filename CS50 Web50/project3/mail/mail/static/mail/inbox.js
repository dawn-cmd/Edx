document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
    document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
    document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
    document.querySelector('#compose').addEventListener('click', compose_email);

    // Sent the email
    document.querySelector('#compose-form').onsubmit = () => {
		let recipients = document.querySelector('#compose-recipients').value;
		let subject = document.querySelector('#compose-subject').value;
		let body = document.querySelector('#compose-body').value;
		fetch('/emails', {
  			method: 'POST',
  			body: JSON.stringify({
      			recipients: recipients,
      			subject: subject,
      			body: body,
  			})
		})
		.then(response => response.json())
		.then(result => {
            console.log(result);
   		 	// Print result
            if (result.error === undefined) {
                alert(result["message"]);
                load_mailbox('sent');
            }
            else {
                alert(result["error"]);
            }
		});
		return false;
    };

    // By default, load the inbox
    load_mailbox('inbox');
});

function compose_email() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#email-display').style.display = 'none';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
	console.log(`${mailbox} has been clicked`);
  
    // Show the mailbox and hide other views
    document.querySelector('#emails-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#email-display').style.display = 'none';

    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
    fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails);
        if (emails.error !== undefined) {
            alert(emails.error);
        }
        else {
            for (i = 0; i < emails.length; ++i) {
                let box = document.createElement('div');
                let left = document.createElement('div');
                let right = document.createElement('div');
                left.innerHTML = `<b>${emails[i].sender}</b> ${emails[i].subject}`;
                left.style.cssText = "text-align: left; float: left;";
                right.innerHTML = `${emails[i].timestamp}`;
                right.style.cssText = "text-align: right; font-weight: lighter; float: right;";
                box.append(left);
                box.append(right);
                if (emails[i].checked == false) {
                    box.style.cssText = "border:2px; border-style:solid; border-color:black; height: 30px; padding: 2px; background-color: white";
                }
                else {
                    box.style.cssText = "border:2px; border-style:solid; border-color:black; height: 30px; padding: 2px; background-color: silver"
                }
                let link = document.createElement('a');
                link.append(box);
                let id = emails[i].id;
                link.onclick = () => email_display(`${id}`, mailbox);
                link.href = "#"; 
                link.style.cssText = "color: black;";
                document.querySelector("#emails-view").append(link);
            }
        }
        // ... do something else with emails ...
    });
}

function email_display(e_id, mailbox) {
    fetch(`/emails/${e_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            checked: true
        })
    });

    document.querySelector('#email-display').style.display = 'block';
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';

    fetch(`/emails/${e_id}`)
    .then(response => response.json())
    .then(email => {
        // Print email
        console.log(email);

        // ... do something else with email ...
        document.querySelector('#d-sender').innerHTML = `<b>From: </b>${email.sender}`;
        document.querySelector('#d-recipient').innerHTML = `<b>To: </b>${email.recipients}`;
        document.querySelector('#d-subject').innerHTML = `<b>Subject: </b>${email.subject}`;
        document.querySelector('#d-timestamp').innerHTML = `<b>Timestamp: </b>${email.timestamp}`;
        document.querySelector('#d-body').innerHTML = email.body;
        if (mailbox === 'sent') {
            document.querySelector('#d-archived').style.display = 'none';
        }
        else if (mailbox === 'inbox' && email.archived === false) {
            document.querySelector('#d-archived').style.display = 'block';
            document.querySelector('#d-archived').innerHTML = 'Archived';
            document.querySelector('#d-archived').onclick = () => {
                fetch(`/emails/${e_id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        archived: true
                    })
                }); 
                load_mailbox('inbox');
            };
        }
        else if (mailbox === 'archive' && email.archived === true) {
            document.querySelector('#d-archived').style.display = 'block';
            document.querySelector('#d-archived').innerHTML = 'Unarchived';
            document.querySelector('#d-archived').onclick = () => {
                fetch(`/emails/${e_id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        archived: false
                    })
                }); 
                load_mailbox('inbox');
            };
        }

        document.querySelector('#d-reply').onclick = () => {
            compose_email();
            document.querySelector('#compose-recipients').value = email.sender;
            document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote:
            ${email.body}`;
            if (email.subject.indexOf('Re: ') !== 0) {
                document.querySelector('#compose-subject').value = `Re: ${email.subject}`;
            }
            else {
                document.querySelector('#compose-subject').value = email.subject;
            }
        }
    });
    
    return false;
}