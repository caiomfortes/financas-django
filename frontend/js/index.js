$(document).ready(function() {
    $('#toggle-password').click(function() {
      let passwordField = $('#password');
      let passwordFieldType = passwordField.attr('type');
      
      // Toggle between 'password' and 'text'
      if (passwordFieldType == 'password') {
        passwordField.attr('type', 'text');
        $(this).html('<i class="fa fa-eye-slash"></i>'); // Change to eye-slash icon
      } else {
        passwordField.attr('type', 'password');
        $(this).html('<i class="fa fa-eye"></i>'); // Change back to eye icon
      }
    });
  });