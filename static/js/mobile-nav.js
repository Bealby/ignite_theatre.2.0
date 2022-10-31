// FULL SCREEN OVERLAY FOR MOBILE

// Open navbar when toggle clicked on mobile
function openMenu(){
  document.getElementById("navbar").style.height = "100%";
}

// Open cast menu when clicked
function openMenuCast(){
  document.getElementById("navbar-cast").style.height = "100%";
}

// Open gallery menu when clicked
function openMenuGallery(){
  document.getElementById("navbar-gallery").style.height = "100%";
}

// Close menu for mobile
function closeMenu(){
  document.getElementById("navbar").style.height = "0%";
}

// Close gallery menu when "back" button clicked
function closeMenuGallery (){
  document.getElementById("navbar-gallery").style.height = "0%";
}

// Close cast menu when "back" button clicked
function closeMenuCast (){
  document.getElementById("navbar-cast").style.height = "0%";
}

// Close all menus when cross clicked
function closeAllMenu (){
  document.getElementById("navbar-gallery").style.height = "0%";
  document.getElementById("navbar").style.height = "0%";
  document.getElementById("navbar-cast").style.height = "0%";
}