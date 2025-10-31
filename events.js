// TODO: replace this sample array only if you reach the stretch goal

console.log("file loaded");

const events = [
  { title: 'Youth Coding Club', date: '2025-05-07', time: '16:00', venue: 'The Hive' },
  { title: 'Community Hackathon', date: '2025-05-14', time: '10:00', venue: 'Town Hall' },
  { title: 'Accessibility Workshop', date: '2025-05-21', time: '13:30', venue: 'Library Hub' }
];



// Your code below ↓
  const cardInfoItems = document.querySelectorAll('.cardInfo');
  let I = 0;
  let Y = 0;

 

  while (I < events.length){

    var cardTitle = events[I].title;
    var cardDate = events[I].date;
    var cardTime = events[I].time;
    var cardVenue = events[I].venue;

      I++
      document.getElementById("events-list").insertAdjacentHTML('beforeend', ' <li class="eventCard"> <ul class="infoHolder"> <li class= "cardInfo"> ' + cardTitle + ' </li> <li class="cardInfo"> ' + cardDate + ' </li> <li class="cardInfo"> ' + cardTime + ' </li> <li class="cardInfo"> ' + cardVenue + ' </li> </ul > </li> ');

    }





    function search(text){
        //if (){}
    }

