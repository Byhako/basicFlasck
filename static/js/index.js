$( document).ready(function() {
  function ajax_login() {
    $.ajax({
      url: '/ajax_login',
      data: $('form').serialize(),
      type: 'POST',
      success: function(resp) {
        console.log(resp)
        $('#login_form')[0].reset()
      },
      error: function(error) {
        console.log(error)
      }
    })
  }

  $('#login_form').submit(function(e) {
    // e.preventDefault()
    ajax_login()
  })
})