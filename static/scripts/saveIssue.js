var csrf = document.getElementsByName('csrfmiddlewaretoken');

function saveIssue() {
    const issueName = event.target.value;

    $.ajax({
        type: 'post',
        url: '/saveissue/',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'name': issueName,
        },
        dataType: 'json',
        success: function(response) {
            saved(issueName, response.value);
        },
        error: function(error) {
            console.log(error);
            alert('Oops, something went wrong!');
        }
    })
}

function saved(issueName, value) {
    if (value === 1) {
        alert("Added" + issueName);
    } else {
        alert("removed" + issueName);
    }
}