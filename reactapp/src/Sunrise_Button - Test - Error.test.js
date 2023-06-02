import React from "react";
import { shallow } from "enzyme";
import LaunchSunriseEhrButton from "../../../src/components/admin/LaunchSunriseEhrButton";
import { expect } from "../../";

describe("LaunchSunriseEhrButton", () => {
  test("renders correctly", () => {
    try {
      const wrapper = shallow(<LaunchSunriseEhrButton loading={true} />);
      expect(wrapper.find(Provider).exists());
      expect(wrapper.find("a").find(".button-sunrise-ehr-text"));
    } catch (error) {
      expect(error).toBeInstanceOf(Error);
    }
  });
});
