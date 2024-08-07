//Write a JavaScript script that fetches the character name,
//from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json,
//The name must be displayed in the HTML tag DIV#character.

let url =('https://swapi-api.alx-tools.com/api/people/5/?format=json');
$.get(url, function(data){
 $('div#character').text(data.name);
});
