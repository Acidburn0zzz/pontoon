$(function() {

  // Update project if already set
  var project = $('#server').data('project'),
      spin = 'fa fa-refresh fa-spin';
  if (project) {
    $('.project-name[data-slug="' + project + '"]').parents('li').click();
  }

  // Update locale if already set
  var locale = $('#server').data('locale');
  if (locale) {
    locale = locale.toLowerCase();
    $('.locale .language.' + locale).parents('li').click();
  }

  $('#project-load').hide();
  $('#intro').css('display', 'table').hide().fadeIn();

  // Authentication and profile menu
  $("#browserid").click(function(e) {
    $('#loading').toggleClass(spin).empty();
    e.preventDefault();
    var redirect = $('#server').data('redirect');

    navigator.id.get(function(assertion) {
      if (assertion) {
        $.ajax({
          url: 'browserid/',
          type: 'POST',
          data: {
            assertion: assertion,
            csrfmiddlewaretoken: $('#server').data('csrf')
          },
          success: function(data) {
            if (data !== 'error') {
              if (redirect) {
                window.location = redirect;
                return;
              }
              $('#action').remove();
              $('#signout').removeClass('hidden').find('a').attr('title', data.browserid.email);
              if (data.manager) {
                $('#admin').removeClass('hidden');
              }
              $('form').removeClass('hidden');
              $('.notification').addClass('hidden');
            } else {
              $('.notification').html('<li>Oops, something went wrong.</li>').removeClass('hidden');
              $('#loading').toggleClass(spin).html('or');
            }
          },
          error: function() {
            $('.notification').html('<li>Oops, something went wrong.</li>').removeClass('hidden');
            $('#loading').toggleClass(spin).html('or');
          }
        });
      } else {
        $('#loading').toggleClass(spin).html('or');
      }
    });
  });

});
