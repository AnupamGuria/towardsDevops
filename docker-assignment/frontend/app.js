import axios from "axios";
import express from "express";
const app = express();
const port = 3000;
const host = "0.0.0.0";

app.set("view engine", "ejs");
app.use(express.urlencoded({ extended: true }));

const URL = process.env.BACKEND_URL || "http://127.0.0.1:5000/submit";

// Render the form
app.get("/", (req, res) => {
  res.render("index");
});

// Handle form submission
app.post("/submit", async (req, res) => {
  const formData = req.body;

  //console.log(formData.name);
  //res.send(`Received: Name = ${name}, Email = ${email}`);

  // Send POST request to another backend using fetch (it is older method)
  // const response =fetch(URL, {
  //   method: "POST",
  //   headers: { "Content-Type": "application/json" },
  //   body: JSON.stringify(formData),
  // })
  //   //.then((data) => console.log(data))
  //   .then(() => res.render("submit", { message:"Data submitted"}))
  //   .catch((err) => console.error(err));

  // Send data to another backend using axios
  const response = await axios.post(URL, formData);
  res.render("submit", {message:response.data});
});

app.listen(port, host, () => {
  console.log(`Server running at http://localhost:${port}`);
});
