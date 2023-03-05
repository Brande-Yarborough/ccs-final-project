import "./App.css";

function App() {
  const [albums, setAlbums] = useState(null);

  //fetch request
  const fetch = async () => {
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": Cookies.get("csrftoken"),
      },
      body: JSON.stringify(albums),
    };

    const response = await fetch("/api_v1/albums/", options);
    if (!response.ok) {
      throw new Error("Network response not ok.");
    }

    const data = await response.json();
    // console.log({ data });
    setAlbums([...albums, data]);
  };

  if (!articles) {
    return <div>Fetching data ...</div>;
  }

  return (
    <div className="App">
      <button onclick={fetch}>I am button</button>
    </div>
  );
}

export default App;
