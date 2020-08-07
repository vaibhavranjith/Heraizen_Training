headings=["Team","Played","Won","Lost","Net RR","Points"];
let admins=[
    {
        "e-mail":"vax@gmail.com",
        "password":"vaibhav"
    },
    {
        "e-mail":"ghost@gmail.com",
        "password":"ghosting"
    }
];
let teams=[
    {
        name:"Mumbai Indians",
        played:14,
        won:9,
        lost:5,
        net_rr:+0.42,
        pts:18
    },
    {
        name:"Chennai Super Kings",
        played:14,
        won:9,
        lost:5,
        net_rr:+0.131,
        pts:18
    },
    {
        name:"Delhi Capitals",
        played:14,
        won:9,
        lost:5,
        net_rr:+0.044,
        pts:18
    }
]
let teamindex=-1;
const btnadd=document.querySelector("#btnAdd");
const btnUpdate=document.querySelector("#btnUpdate")
function addteam(){ 
    teams.push({ name:document.getElementById("team").value,
                    played:document.getElementById("played").value,
                    won:document.getElementById("won").value,
                    lost:document.getElementById("lost").value,
                    net_rr:document.getElementById("netrr").value,
                    pts:document.getElementById("points").value
    });
    displaytables("alter_content",true); 
    console.log("oasnfd");
}


btnadd.addEventListener('click', (event) => {
    // event.preventDefault();
    teams.push({ name:document.getElementById("team").value,
                    played:document.getElementById("played").value,
                    won:document.getElementById("won").value,
                    lost:document.getElementById("lost").value,
                    net_rr:document.getElementById("netrr").value,
                    pts:document.getElementById("points").value
    }); 
    init();
})

btnUpdate.addEventListener('click',(event)=>{
    event.preventDefault();
    if (teamindex > -1) {
        console.log("hey");
        let temp={  name:document.getElementById("team").value,
                    played:document.getElementById("played").value,
                    won:document.getElementById("won").value,
                    lost:document.getElementById("lost").value,
                    net_rr:document.getElementById("netrr").value,
                    pts:document.getElementById("points").value};
        teams[teamindex] = temp;
    }
    init();
})
function deleteContact(name){
    console.log("delete");
    teams = teams.filter((teams) => teams.name !== name);
    init();
}
function init(){
    document.querySelector("#btnAdd").removeAttribute('disabled');
    document.querySelector("#btnUpdate").setAttribute('disabled', true);
    document.querySelector("#played").removeAttribute('disabled');
    document.querySelector("#won").removeAttribute('disabled');
    document.querySelector("#lost").removeAttribute('disabled');
    document.querySelector("#netrr").removeAttribute('disabled');
    document.querySelector("#points").removeAttribute('disabled');
    displaytables("alter_content",true);
    teamindex=-1;
}

function altertable(){
    init();
    let id_="alter_content";
    displaytables(id_,true);
    // location.reload();

}

const editTeam = function (name) {
    console.log("Edit is clicked");
    teamObj = teams.filter(ele => ele.name ===name )[0];
    document.querySelector("#btnUpdate").removeAttribute('disabled');
    document.querySelector("#btnAdd").setAttribute('disabled', true);
    document.querySelector("#played").setAttribute('disabled', true);
    document.querySelector("#won").setAttribute('disabled', true);
    document.querySelector("#lost").setAttribute('disabled', true);
    document.querySelector("#netrr").setAttribute('disabled', true);
    document.querySelector("#points").setAttribute('disabled', true);
    if (teamObj) {
        document.getElementById("team").value = teamObj.name;
        document.getElementById("played").value = teamObj.played;
        document.getElementById("won").value = teamObj.won;
        document.getElementById("lost").value = teamObj.lost;
        document.getElementById("netrr").value = teamObj.net_rr;
        document.getElementById("points").value = teamObj.pts;
        teamindex=teams.indexOf(teamObj);
    }
}

function loginval(){
    let e=document.getElementById("email").value;
    let p=document.getElementById("password").value;
    for(let i=0;i<admins.length;i++){
        if(e==admins[i]["e-mail"] && p==admins[i]["password"] ){
            console.log("login");   
            setCookie("loggedin",true);
            location.replace("index.html");
        }
    }    
}

function setCookie(cname,cvalue){
    document.cookie=cname+"="+cvalue+";path=/";
}
function getCookie(cname){
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

function logout(){
    setCookie("loggedin",false);
    location.replace("index.html");
    alert("You have succcesfully logged out!")
}



function displaytables(id_,logstate){
    let table = "<table class='table table-striped table-dark table-responsive-sm'>";
    // table += "<th>";
    headings.forEach(h => {
        table += `<th>${h}</th>`
    })
    table += "</th>";
    teams.forEach(c => {
        table += "</tr>";
        if(logstate){
            table += `<td>${c.name}</td><td>${c.played}</td><td>${c.won}</td><td>${c.lost}</td><td>${c.net_rr}</td><td>${c.pts}</td>
            <td>
            <button class="edit-btn" onclick="editTeam('${c.name}')">E</button>  
            <button class="trash-btn" onclick="deleteContact('${c.name}')">D</a></button>`;
        }
        else{
            table += `<td>${c.name}</td><td>${c.played}</td><td>${c.won}</td><td>${c.lost}</td><td>${c.net_rr}</td><td>${c.pts}</td>`;
        }
        table += "</tr>";
    })
    table += "</table>";
    document.getElementById(id_).innerHTML=table;
}

function teamtable(){
    let id_="content"
    displaytables(id_,false);
    if(getCookie("loggedin")=="true"){
        document.getElementById("login_privilege").innerHTML+="<a class=\"nav-link\" href=\"alter.html\">ALTER</a>"
        // document.getElementById("login_privilege_alter").innerHTML+="<a class=\"nav-link\" href=\"alter.html\">ALTER</a>"
        document.getElementById("log_out").innerHTML+="<a class=\"nav-link logout-btn\" href=\"#\" onclick=\"logout()\">LOG-OUT</a>"
        // document.getElementById("log_out_alter").innerHTML+="<a class=\"nav-link logout-btn\" href=\"#\" onclick=\"logout()\">LOG-OUT</a>"
    }

}