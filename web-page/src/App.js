import "./App.css";
import UpperBar from "./components/UpperBar/UpperBar.jsx";
import { Footer } from "./components/Footer/Footer";
function App() {
  return (
    <>
      <UpperBar></UpperBar>
      <div className="h-screen flex flex-col">
        <main className="flex-grow"></main>

        <Footer></Footer>
      </div>
    </>
  );
}

export default App;
