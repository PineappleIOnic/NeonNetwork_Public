function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
  for(var i = 0; i <ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function changeBackgroundFunc(backgroundCookie) {
  switch (backgroundCookie) {
    case "1":
      document.body.style.backgroundImage = "linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB)";
      document.cookie = "background=1; path=/;";
      break;
    case "2":
      document.body.style.backgroundImage = "linear-gradient(-45deg, #f93f3f, #ef7d3b, #efb63b, #ffee3d)";
      document.cookie = "background=2; path=/;";
      break;
    case "3":
      document.body.style.backgroundImage = "linear-gradient(-45deg, #51ff6b, #58fcaf, #58fcf6, #58b4fc)";
      document.cookie = "background=3; path=/;";
      break;
    case "4":
      document.body.style.backgroundImage = "linear-gradient(-45deg, #403da5, #4b1296, #b738ad, #720d3b)";
      document.cookie = "background=4; path=/;";
      break;
    case "5":
      document.body.style.backgroundImage = "linear-gradient(-45deg, #323b68, #1b2242, #1a1e33, #2e3451)";
      document.cookie = "background=5; path=/;";
      break;
    default:
      document.body.style.backgroundImage = "linear-gradient(-45deg, #EE7752, #E73C7E, #23A6D5, #23D5AB)";
      document.cookie = "background=1; path=/;";
    }
}
