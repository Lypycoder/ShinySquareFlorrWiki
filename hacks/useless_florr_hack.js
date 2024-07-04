// ==UserScript==
// @name        First florr.io script ever
// @namespace   -
// @version     1.1.6
// @description this does nothing
// @author      dreadmania
// @include     *://florr.io/*
// @connect     florr.io
// @grant       none
// @require http://code.jquery.com/jquery-latest.js
// ==/UserScript==
 
$(document).ready(function() {  alert('This script does nothing. It could soon. Just let me learn javascript.');});
var hrefs = new Array();
var elements = $('.headline > a');
elements.each(function() {
  hrefs.push($(this).attr('href'));
});
 
$('body').append('<input type="button" value="Does this do anything" id="CP">')
$("#CP").css("position", "fixed").css("top", 0).css("left", 0);
 
$('#CP').click(function(){
  $.each(hrefs, function(index, value) {
      alert('What are you thinking of?!');
  });
});