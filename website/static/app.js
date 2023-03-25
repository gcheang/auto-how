let isQuiz = false;

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function generateResponse(prompt) {
  return new Promise((resolve, reject) => {
    fetch("/generate-response", {
      method: "POST",
      body: JSON.stringify({ text: prompt }),
    })
      .then((response) => response.json())
      .then((data) => {
        // access the properties of the JSON object
        console.log(data.resp);

        // resolve the Promise with property1
        resolve(data);
      })
      .catch((error) => {
        // reject the Promise with the error message
        reject(error.message);
      });
  });
}

function generateSummary() {
  return new Promise((resolve, reject) => {
    fetch("/generate-summary", {
      method: "POST",
    })
      .then((response) => response.json())
      .then((data) => {
        // access the properties of the JSON object
        console.log(data.resp);

        // resolve the Promise with property1
        resolve(data.resp);
      })
      .catch((error) => {
        // reject the Promise with the error message
        reject(error.message);
      });
  });

  // fetch('/generate-response', {
  //     method: 'POST',
  //     body: JSON.stringify({ text: prompt })
  // }).then(response => response.json())
  // .then(data => {
  //   console.log(data.resp);
  //   return data.resp;
  // });
}

const textInput = document.querySelector("#message-input");
const submitButton = document.querySelector("#message-submit");
const genSummaryButton = document.querySelector("#gen-summary");
const genQuizButton = document.querySelector("#gen-quiz");

textInput.addEventListener("keydown", inpHandler);
function inpHandler(e) {
  if (e.key === "Enter" && isQuiz === false) {
    addUserMessage();
  }
}

function addUserMessage() {
  const messagesDisplay = document.querySelector("#messages-display");
  let prompt = textInput.value;
  if (prompt !== "") {
    let ul = document.createElement("ul");
    ul.classList.add("messages");
    let new_li = document.createElement("li");
    new_li.classList.add("user-message");
    new_li.innerText = prompt;
    ul.appendChild(new_li);

    let newMessageHolder = document.createElement("div");
    newMessageHolder.classList.add("message-holder");
    newMessageHolder.classList.add("user-colour");
    newMessageHolder.appendChild(ul);
    messagesDisplay.appendChild(newMessageHolder);

    ul = document.createElement("ul");
    ul.classList.add("messages");
    new_li = document.createElement("li");
    new_li.classList.add("computer-message");
    new_li.innerText = "Generating response...";
    ul.appendChild(new_li);

    newMessageHolder = document.createElement("div");
    newMessageHolder.classList.add("message-holder");
    newMessageHolder.classList.add("computer-colour");
    newMessageHolder.appendChild(ul);
    messagesDisplay.appendChild(newMessageHolder);

    messagesDisplay.scrollTop = messagesDisplay.scrollHeight;

    generateResponse(prompt).then((resp) => {
      console.log(`property1 is: ${resp}`);

      // add response to page
      let inner_content = document.querySelector("#inner-content");
      inner_content.innerHTML = "";

      let h1 = document.createElement("h1");
      h1.id = "prompt-h1";
      //   h1.innerText = "Output:";
      h1.innerText = titleCase(prompt);


      // Add generated stuff
      resp.forEach(element => {
      let p = document.createElement("p");
      p.classList.add("content-paragraphs");
      p.innerText = element["resp"];
      inner_content.appendChild(h1);
      inner_content.appendChild(p);
      if (element["image_url"] !== "") {
        let img = document.createElement("img");
        img.src = element["image_url"];
        img.classList.add("content-images");
        inner_content.appendChild(img);
      }
      });

      // let user know response was generated
      let response = document.createElement("div");
      response.classList.add("message-holder");
      response.classList.add("computer-colour");
      let new_msg = document.createElement("ul");
      new_msg.classList.add("messages");
      let new_msg_content = document.createElement("li");
      new_msg_content.classList.add("computer-message");
      new_msg_content.innerText = "Response Generated!";
      new_msg.appendChild(new_msg_content);
      response.appendChild(new_msg);
      messagesDisplay.appendChild(response);

      messagesDisplay.scrollTop = messagesDisplay.scrollHeight;
    });
  }
  textInput.value = "";
}

function titleCase(str) {
  var splitStr = str.toLowerCase().split(" ");
  for (var i = 0; i < splitStr.length; i++) {
    // You do not need to check if i is larger than splitStr length, as your for does that for you
    // Assign it back to the array
    splitStr[i] =
      splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
  }
  // Directly return the joined string
  return splitStr.join(" ");
}
