const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

function calibrationChange(stack_id) {
  const data = {
    type: "calibChange",
    stack_id: stack_id,
  };
  fetch("", {
    method: "POST",
    body: JSON.stringify(data),

    headers: {
      "X-CSRFToken": csrfToken,
    },
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.response !== "changed") {
        console.error(data.message);
      } else {
        console.log("changed");
      }
    });
}
