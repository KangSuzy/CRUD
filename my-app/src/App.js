// eslint-disable-next-line
import React from "react";
import "./App.css";


const headerStyle = {
  color: "red",
  fontWeight: 800
};

const WorldClock = props => {
  return(
    <div className="WorldClock">
    <h2>
      <span role="img" aria-label="Earth Emoji">
        🌏
      </span>{" "}
      {props.city}
    </h2>
    <p>
      <span role="img" aria-label="Clock Emoji">
        ⏰
      </span>{" "}
      {props.time}
    </p>
  </div>
  );
};

function App() {  const cityTimeData = [
  ['서울', '10:00'],
  ['베이징', '09:00'],
  ['시드니', '12:00'],
  ['LA', '17:00']
];

const WorldClockList = cityTimeData.map((cityTime, idx) => (
  <WorldClock city={cityTime[0]} time={cityTime[1]} key={idx} />
));

return (
  <div className="App">
      <h1 style={headerStyle}>Hello World!</h1>
      <h2 className={'titleStyle'}>ReactJS 둘러보기</h2>
      {WorldClockList}
  </div>
);
}

export default App;