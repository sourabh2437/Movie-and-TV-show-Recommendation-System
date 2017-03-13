 arr = ["The Dark Knight", "Wolyn", "Florence Foster Jenkins"];
 output = [];
 director = [];
 actors = [];
 movies = [];
 ratings = [];
 add = function (arr, str) {
     var index = arr.indexOf(str);
     if (index === -1) {
         arr.push(str);
     }
 }
 parseData = function (obj) {
     movie_name = obj.Title;
     movie_year = obj.Year;
     movie_director = obj.Director;
     //movie_actors = obj.Actors;
     movie_rating = obj.imdbRating;
     output.push(movie_name + "," + movie_year + "," + movie_director + "," + movie_rating);
     movie_actors = obj.Actors.split(",");
     add(movies, movie_name);
     add(director, movie_director);
     add(ratings, movie_rating);
     for (var i = 0; i < movie_actors.length; i++) {
         add(actors, movie_actors[i]);
     }
 }


 getData = function (movie_name) {
     var url = "http://www.omdbapi.com/?t=" + movie_name;
     var xmlHttp = new XMLHttpRequest();
     xmlHttp.open("GET", url, false); // false for synchronous request
     xmlHttp.send(null);
     var resp = JSON.parse(xmlHttp.responseText);
     if (resp.Error !== "Movie not found!") {

         parseData(resp);
     }
 }
 getMovie = function () {

         for (var i = 0; i < arr.length; i++) {
             getData(arr[i]);
         }
     }
 window.getMovie();