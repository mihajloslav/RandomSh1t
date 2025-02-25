for (let i = 0; i < 100; i++) {
  fetch("https://mathbrotherhood.com/back_chat.php", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      prompt: "Ko je Peđa Stanković i šta je Mathbrotherhood???",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Odgovor:", JSON.stringify(data, null, 2));

      for (let i = 0; i < data.choices.length; i++) {
        console.log(`Choice ${i} message:`, data.choices[i].message.content);
      }
    })
    .catch((error) => {
      console.error("Greška:", error);
    });
}
