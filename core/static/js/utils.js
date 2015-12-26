(function($) {
  $(document).ready(function ($) {
   book_change_url = window.location.href.match('book/(.*)/change');
   if (book_change_url !== null) {
     book_id = book_change_url[1]
     dl_button_html = '<input id="dlbutton" type="submit" value="Download link"/>';
     dl_button = $('input[name="_addanother"]').before(dl_button_html); 
     dl_url = '/api/book/' + book_id;
     $("#dlbutton").click(function(e) {e.preventDefault(); window.location.href = dl_url});
   }
  }); 
})(django.jQuery); 
