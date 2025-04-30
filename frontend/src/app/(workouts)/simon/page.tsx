"use client";
import React, { useEffect, useState, useRef } from "react";
import GameBtn from "./GameBtn";
//import { setTimeout } from "timers/promises";

const colors = ["green", "red", "yellow", "blue"];

function SimonPage() {
  const [sequence, setSequence] = useState([]);
  const [playing, setPlaying] = useState(false);
  const [playingIdx, setPlayingIdx] = useState(0);

  const greenRef = useRef(null);
  const redRef = useRef(null);
  const yellowRef = useRef(null);
  const blueRef = useRef(null);

  const resetGame = () => {
    setSequence([]);
    setPlaying(false);
    setPlayingIdx(0);
  };

  const addNewColor = () => {
    const color = colors[Math.floor(Math.random() * 4)];
    const newSequence = [...sequence, color];
    setSequence(newSequence);
  };

  const handleNextLevel = () => {
    if (!playing) {
      setPlaying(true);
      addNewColor();
    }
  };

  const handleColorClick = (e) => {
    if (playing) {
      const clickColor = e.target.getAttribute("color");

      if (sequence[playingIdx] === clickColor) {
        if (playingIdx === sequence.length - 1) {
          setTimeout(() => {
            setPlayingIdx(0);
            addNewColor();
          }, 250);
        } else {
          setPlayingIdx(playingIdx + 1);
        }
      } else {
        resetGame();
      }
    }
  };

  useEffect(() => {
    if (sequence.length > 0) {
      const showSequence = (idx = 0) => {
        let ref = null;

        if (sequence[idx] === "green") ref = greenRef;
        if (sequence[idx] === "red") ref = redRef;
        if (sequence[idx] === "yellow") ref = yellowRef;
        if (sequence[idx] === "blue") ref = blueRef;
        console.log(ref);
        setTimeout(() => {
          ref.current.classList.add("brightness-[2.5]");

          setTimeout(() => {
            ref.current.classList.remove("brightness-[2.5]");
            if (idx < sequence.length - 1) showSequence(idx + 1);
          }, 250);
        }, 250);
      };
      showSequence();
    }
  }, [sequence]);

  return (
    <div className="flex justify-center items-center bg-neutral-800 text-white w-screen h-screen">
      <div className="relative flex flex-col justify-center items-center">
        <div>
          <GameBtn
            color="green"
            border="rounded-tl-full"
            bg="bg-green-500"
            onClick={handleColorClick}
            ref={greenRef}
          />
          <GameBtn
            color="red"
            border="rounded-tr-full"
            bg="bg-red-500"
            onClick={handleColorClick}
            ref={redRef}
          />
        </div>
        <div>
          <GameBtn
            color="yellow"
            border="rounded-bl-full"
            bg="bg-yellow-400"
            onClick={handleColorClick}
            ref={yellowRef}
          />
          <GameBtn
            color="blue"
            border="rounded-br-full"
            bg="bg-blue-500"
            onClick={handleColorClick}
            ref={blueRef}
          />
        </div>
        <button
          className="absolute bg-neutral-900 text-white text-xl sm:text-2xl font-black rounded-full w-[150px] sm:w-[175px] h-[150px] sm:h-[175px] duration-200 hover:scale-105"
          onClick={handleNextLevel}
        >
          {sequence.length === 0 ? "Play" : sequence.length}
        </button>
      </div>
    </div>
  );
}

export default SimonPage;
