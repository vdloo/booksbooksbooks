(function($) {
  $(document).ready(function ($) {
   dl_button_html = '<input id="dlbutton" type="submit" value="Download link"/>';
   dl_button = $('input[name="_addanother"]').before(dl_button_html); 
   book_id = window.location.href.match('book/(.*)/change')[1];
   dl_url = '/api/book/' + book_id;
   $("#dlbutton").click(function(e) {e.preventDefault(); window.location.href = dl_url});
  }); 
})(django.jQuery); 
