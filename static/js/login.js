$(document).ready(function() {

  function ajax_login() {
    $.ajax({
      url: '/ajax-login',
      data: $('form').serialize(),
      type: 'POST',
      success: function(resp) {
        console.log(resp)
      },
      error: function(resp) {
        console.error(resp)
      }
    })
  }

  $('#form-login').submit(function(event) {
    event.preventDefault()
    ajax_login()
  })
})


