var form = document.getElementById("c");

function displayImage() {
  let image = document.getElementById("fimage").value;
  let arr = image.split("\\");
  for (let i = 0; i < arr.length; ++i)
  {
    console.log(arr[i]);
  }
  image = "static/images/" + arr[arr.length - 1];
  localStorage.setItem('wasLoaded', "true");
  localStorage.setItem('image', image);

  const params = {
    image: image
  }
  const options = {
    method: 'POST',
    body: JSON.stringify( params )  ,
    headers: {
      'Content-Type': 'application/json'
    }
  };
  fetch( '/download', options )
  .then( response => response.json() )
  .then( response => {

  } );
}

if (localStorage.getItem('wasLoaded') == "true")
{
  image = localStorage.getItem('image');
  if (image.length > "static/images/".length)
  {
    var img = document.createElement("img");
    img.src = image;
    img.classList.add("hidden");
    var src = document.getElementById("images");
    src.appendChild(img);
  }
}

function register()
{
  const params = {
    email: document.getElementById("register-email").value,
    password: document.getElementById("register-password").value
  };

  const options = {
      method: 'POST',
      body: JSON.stringify( params )  ,
      headers: {
        'Content-Type': 'application/json'
      }
  };
  fetch( '/registering', options )
  .then( response => response.json() )
  .then( response => {

  } );
}

function login() {
  const params = {
    email: document.getElementById("login-email").value,
    password: document.getElementById("login-password").value
  };
  const options = {
    method: 'POST',
    body: JSON.stringify( params )  ,
    headers: {
      'Content-Type': 'application/json'
    }
  };
  fetch( '/login', options )
  .then( response => response.json() )
  .then( response => {

  } );
}