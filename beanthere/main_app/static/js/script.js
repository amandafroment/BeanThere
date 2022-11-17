function selectedButton(evt) {
    console.log(evt)
  let evtVal = `${evt}val`;
      console.log(evtVal)
  displayBtn = document.getElementById(evt);
  dataVal = document.getElementById(evtVal);
  if (dataVal.value === "false") {
    console.log(dataVal.value);
    displayBtn.style.backgroundColor = "#4e4235";
    dataVal.value = "true";
  } else {
    console.log(dataVal.value);
    displayBtn.style.backgroundColor = "#a4978a";
    dataVal.value = "false";
  }
}
