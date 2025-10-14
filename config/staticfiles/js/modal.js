$(document).ready(function(){
    // when the modal is shown
    $("#deleteConfirmationModal").on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget); // Button that triggered the modal
        const contactId = button.data('id'); // Extract info from data-* attributes
        const deleteUrl = button.data('url'); // Extract delete URL
        $("#modal-contact-id").text(contactId);
        // set the delete URL
        $("#delete-contact-form").attr('href', deleteUrl);
    });
    // when the delete button is clicked, submit the form
    $("#confirm-delete-btn").click(function(event){
        // close the modal
        $("#deleteConfirmationModal").modal('hide');
        setTimeout(() => {
            window.location.href = $("#delete-contact-form").attr('href');
        },300);
    });
});