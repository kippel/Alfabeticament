import React, { forwardRef } from "react";

type Props = {
  border: string;
  bg: string;
  onClick?: (e: any) => void;
  color: string;
};

const GameBtn = forwardRef<HTMLAnchorElement, Props>(
  ({ color, border, bg, onClick }, ref) => (
    <button
      color={color}
      className={`${border} ${bg} w-[175px] sm:w-[200px] h-[175px] sm:h-[200px] m-2 duration-200 hover:scale-105`}
      onClick={onClick}
      ref={ref}
    />
  )
);

export default GameBtn;
