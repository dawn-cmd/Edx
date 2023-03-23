document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('form').onsubmit = () => {
        fetch('http://api.exchangeratesapi.io/v1/latest?access_key=f3243f7f87f88a9470e5e8432a4c31ca').then(response => response.json()).then(data => {
            const ori_currency = document.querySelector('#originalcurrency').value.toUpperCase();
            const t_currency = document.querySelector('#targetcurrency').value.toUpperCase();
            if (data.rates[ori_currency] !== undefined && data.rates[t_currency] !== undefined) {
                document.querySelector('#result').innerHTML = `1 ${ori_currency} equals to ${data.rates[t_currency] / data.rates[ori_currency]} ${t_currency}.`;
            }
            else {
                document.querySelector('#result').innerHTML = 'Invalid currency.'
            }
            
        });
        return false;
    }

    
    
});