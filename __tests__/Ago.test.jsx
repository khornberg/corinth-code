import { expect, test, afterEach } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import Ago from "../components/ago";

afterEach(cleanup);

test("ago compoment", () => {
  const current = new Date(Date.parse("2022-06-24T12:24:32Z"));
  render(
    <Ago
      text="Long Ago:"
      timeInThePast="2022-06-22T06:00:00Z"
      current={current}
    />
  );
  const main = screen.getByText("Long Ago:");
  expect(main.innerHTML).toContain("2 days ago");
});
