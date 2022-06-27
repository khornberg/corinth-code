import { expect, test, afterEach } from "vitest";
import { render, screen, cleanup } from "@testing-library/react";
import Error from "../components/error";

afterEach(cleanup);

test("error compoment", () => {
  render(<Error />);
  const error = screen.getByText("Something broke a short short time ago");
});
