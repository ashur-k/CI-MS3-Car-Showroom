//Initialising side nav with materialize
console.log('testing')

    const slide_menu= document.querySelector(".sidenav");
    M.Sidenav.init(slide_menu,{});
//Slider
  const slider = document.querySelector('.slider');
  M.Slider.init(slider, {
      indicators: false,
      height: 500,
      transition: 500,
      interval: 6000
  });
   $( document ).ready(function() {
$('.dropdown-trigger').dropdown();
});

 //material boxed
  const mb = document.querySelectorAll('.materialboxed');
  M.Materialbox.init(mb,{})

   const ss = document.querySelectorAll('.scrollspy');
  M.Scrollspy.init(ss,{})


document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var options = { coverTrigger: false  }
    var instances = M.Dropdown.init(elems, options);
  });
 