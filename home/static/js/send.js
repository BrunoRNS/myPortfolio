document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitBtn = document.getElementById('submitBtn');
    const formData = new FormData(form);
    
    submitBtn.disabled = true;
    
    try {
        const response = await fetch('/send/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            }
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.errors || 'Failed to send');
        }
        
        alert('Message sent successfully!');
        form.reset();
    } catch (error) {
        alert('Error: ' + (error.message || 'Please try again later'));
    } finally {

        submitBtn.disabled = false;
        submitBtn.querySelector('p').textContent = 'Send';
    }
});