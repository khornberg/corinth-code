import { expect, test, afterEach } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import Landing from "../pages/index";

afterEach(cleanup);

test("landing page empty", () => {
  render(<Landing />);
  const main = screen.getByRole("landing");
  expect(main.innerHTML).toContain("for Your Favorite");
  expect(main.innerHTML).toContain("Search");
  const form = screen.getByPlaceholderText("What is wookie?");
  expect(form.value).toBe("");
});
