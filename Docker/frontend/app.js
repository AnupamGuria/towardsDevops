const express = require("express");
const app = express();
const host = "0.0.0.0";
const PORT = 3000;

app.set("view engine", "ejs");

const URL = process.env.BACKEND_URL || "http://localhost:8000/api";

const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));

app.get("/", async function (req, res) {
  const options = {
    method: "GET",
  };
  fetch(URL, options)
    .then((res) => res.json())
    .then((json) => console.log(json))
    .catch((err) => console.error("error:" + err));
  try {
    let response = await fetch(URL, options);
    response = await response.json();
    res.render("index", response);
  } catch (err) {
    console.log(err);
    res.status(500).json({ msg: `Internal Server Error.` });
  }
});

app.listen(PORT, host, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
