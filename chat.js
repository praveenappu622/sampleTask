var style = document.createElement('style');
style.innerHTML = `

*{
    margin: 0;
    padding: 0;
    outline: 0;
    box-sizing: border-box;
    font-family: 'Mulish', sans-serif;
  }

  .chatbot_icon {
    height: 100px;
    width: 100px;
    background-color: #1581c9;
    border-radius: 50%;
    position: fixed;
    bottom: 20px;
    right: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: all 1s;
    animation: moving 1s ease-in-out infinite alternate;
  }

  .chatbot_icon img{
    height:140px;
    width:100px;
  }

  @keyframes moving {
    0% {
      transform: translateY(-20px);
    }
    100% {
      transform: translateY(0px)
    }
  }

  .chat-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 400px;
    height: 500px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    font-family: Arial, sans-serif;
    display: none;
  }

  .chat-header {
    background-color: #1581c9;
    color: #fff;
    padding: 15px;
    text-align: center;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    display: flex;
    align-items: center;
    width: 100%;
    justify-content: space-between;
  }

  .chat-header img {
    height: 20px;
    width: 20px;
    filter: invert(1);
    cursor: pointer;
  }

  .chat-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 10px;
    overflow-y: auto;
  }

  .chat-messages {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 30px;
    overflow-y: scroll;
    scrollbar-width: none;
  }

  .input-container {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
    align-items: center;
    max-height: 120px;
    overflow-y: auto;
    border-top: 0.5px solid rgba(128, 128, 128, 0.645);
  }

  #chat-input {
    width: 90%;
    height: auto;
    min-height: 30px;
    resize: none;
    border: none;
    padding: 10px;
    box-sizing: border-box;
    scrollbar-width: none;
  }

  .send-message-icon {
    border: none;
    outline: none;
    cursor: pointer;
    margin-top: 5px;
    display: none;
  }

  .send-message-icon img {
    height: 25px;
    width: 25px;
  }

  #chat-input:focus + .send-message-icon {
    display: flex;
  }

  .messageBoxContainer {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 10px;
    align-items: flex-end;
  }

  .user {
    background-color: #1581c9;
    align-self: flex-end;
    padding: 10px;
    border-radius: 10px 0px 10px 10px;
    color: white;
  }

  .chitti_the_bot {
    background-color: lightgray;
    padding: 10px;
    border-radius: 0px 10px 10px 10px;
    align-self: flex-start;
  }

  .sender_user {
    color: #000;
    align-self: flex-end;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .sender_bot {
    color: #000;
    align-self: flex-start;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .loader_hide {

    margin-right: 5px;
    display: none;

  }

  .loader_show{
    display: block;
  }

`;

// Append styles to head
document.head.appendChild(style);



// Create chatbot icon
var chatbotIcon = document.createElement('div');
chatbotIcon.classList.add('chatbot_icon');

var img = document.createElement('img');
img.src = "https://i.ibb.co/KW77m7n/robo1.png";


chatbotIcon.appendChild(img);

// Create chat container
var chatContainer = document.createElement('div');
chatContainer.classList.add('chat-container');

// Create chat header
var chatHeader = document.createElement('div');
chatHeader.classList.add('chat-header');

var h3 = document.createElement('h3');
h3.textContent = "Chatify Bot";

var closeImg = document.createElement('img');
closeImg.src = "https://i.ibb.co/FbfJjR8/close.png";

chatHeader.appendChild(h3);
chatHeader.appendChild(closeImg);

// Create chat body
var chatBody = document.createElement('div');
chatBody.classList.add('chat-body');

var chatMessagesDiv = document.createElement('div');
chatMessagesDiv.classList.add('chat-messages');

var chatBotTextLoader = document.createElement('p');
chatBotTextLoader.textContent = "Chitti the Bot is typing...";
chatBotTextLoader.classList.add('loader');
chatBotTextLoader.classList.add('loader_hide');

var inputContainer = document.createElement('div');
inputContainer.classList.add('input-container');

var textarea = document.createElement('textarea');
textarea.id = "chat-input";
textarea.rows = "1";
textarea.placeholder = "Type your message...";

var button = document.createElement('button');
button.classList.add('send-message-icon');

var img = document.createElement('img');
img.src = "https://i.postimg.cc/2SVpMyGT/send-message.png";

button.appendChild(img);

inputContainer.appendChild(textarea);
inputContainer.appendChild(button);

chatBody.appendChild(chatMessagesDiv);
chatBody.appendChild(inputContainer);

chatContainer.appendChild(chatHeader);
chatContainer.appendChild(chatBody);

// Create chatbot div
var chatbotDiv = document.createElement('div');
chatbotDiv.classList.add('chatbot-div');
chatbotDiv.appendChild(chatbotIcon);
chatbotDiv.appendChild(chatContainer);

// Append chatbot div to body
document.body.appendChild(chatbotDiv);


const chatMessages = document.querySelector('.chat-messages');
const chatInput = document.querySelector('#chat-input');
const Input_container = document.querySelector('.input-container');

const sendButton = document.querySelector('.send-message-icon');
const chat_container = document.querySelector('.chat-container');
const chat_container_close = document.querySelector('.chat-header img');

const chatBot_icon = document.querySelector('.chatbot_icon');
const chatBotTextBox = document.querySelector('.loader');



// Sample responses for the chatbot
const responses = [
  'Hello! How can I assist you today?',
  'I\'m an AI chatbot designed to help you with your queries.',
];




chatBot_icon.addEventListener("click",()=>{

  chat_container.style.display = "flex";

})

chat_container_close.addEventListener("click",()=>{

  chat_container.style.display = "none";
})


chatInput.addEventListener("input",(e)=>{

  let prompt = e.target.value;

    if (prompt.length > 0){
      sendButton.style.display ="flex"
    }else{
      sendButton.style.display ="none"
    }
})

const maxHeight = 120; // Set a specific max-height value
chatInput.addEventListener('input', function(e) {

  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px';

  // Limit the maximum height
  // const maxHeight = parseInt(window.getComputedStyle(this).getPropertyValue('max-height'));

  console.log("scrollHeight",this.scrollHeight);
  console.log("maxHeight",maxHeight);

  if (this.scrollHeight > maxHeight) {
    this.style.overflowY = 'scroll';
    this.style.height = maxHeight + 'px';
  } else {
    this.style.overflowY = 'hidden';
  }

  let prompt = e.target.value;

    if (prompt.length > 0){
      sendButton.style.display ="flex"
      Input_container.classList.add("focus_shadow")
    }else{
      sendButton.style.display ="none"
      Input_container.classList.remove("focus_shadow")
    }

});



// Function to display a message in the chat
function displayMessage(message, sender) {

  const messageDiv = document.createElement('div');

  messageDiv.classList.add("messageBoxContainer")

  const senderClass = sender === 'user' ? 'sender_user' : 'sender_bot';
  const sendericon = sender === 'user' ? 'https://i.ibb.co/BPQggCs/user.png' : 'https://i.ibb.co/kXYXsS5/robot.png';

  messageDiv.innerHTML = `

    <div class="${senderClass}">
    <img src="${sendericon}" height="25px" width="25px">
     <p >${sender}</p>
    </div>
    <p class="${sender}" >${message}</p>
  `

  // chatMessages.appendChild(messageSenderName);
  chatMessages.appendChild(messageDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  sendButton.style.display ="none"
}

// Function to generate a random response from the chatbot
function getRandomResponse() {
  return responses[Math.floor(Math.random() * responses.length)];
}

// Display the initial greeting from the chatbot
displayMessage(getRandomResponse(), 'chitti_the_bot');

// Event listener for sending a message
sendButton.addEventListener('click', async () => {
    let isParamsEmpty = false;
    let emptyParams ="";

    const message = chatInput.value.trim();

    if (message) {
      displayMessage(message, 'user');
  
      chatBotTextBox.classList.remove('loader_hide');
      chatBotTextBox.classList.add('loader_show');
    
      let params = JSON.parse(localStorage.getItem("params"));
  
      if (params) {
        let keys = Object.keys(params);
        keys.forEach(key => {
          if (params[key] === "") {
            isParamsEmpty= true;
            emptyParams = key
            return;
          }
        });
      }
  
      if(isParamsEmpty == true){
  
        console.log(`${emptyParams} value is empty or null`);
  
      }else{
  
        let apiResponse = await SendQuery(message, params);
  
          if (apiResponse.Success) {
            let formattedText = apiResponse.Success.replace(/\\n/g, "<br>");
            displayMessage(formattedText, 'chitti_the_bot');
          } else {
            console.log("Error while fetching response!", apiResponse);
          }
  
      }
  
      chatBotTextBox.classList.remove('loader_show');
      chatBotTextBox.classList.add('loader_hide'); // Hide loader after response received
      chatInput.value = '';
    }
  });

  async function SendQuery(message,params) {

    console.log("mesaaaage =>",message)
  
    return  await fetch("http://192.168.1.4:4500/chatQuery", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
  
        "apiKey":"hV6R1XxhbzaBoiL2LAthifEb+5Imq+Hwjj1V/Pvi6Hf+oxl3YSei4bdagB+ExMtmTM1XcqR2mPlTkdEtNHsjG87S4/4EOMLO8cGwK4/L3qs=",
        "userQuery":message,
        "requestedType":"PLUGIN",
        "userId": "1234",
        "params":params
      
      })
    })
    .then(response => response.json())
      .then(result => {
  
        console.log("Response Query", result);
        return result
  
      })
      .catch(error => {
        // Handle any errors that occur during the fetch
        console.error('Error fetching data:', error);
      })
  
      
  }
  
