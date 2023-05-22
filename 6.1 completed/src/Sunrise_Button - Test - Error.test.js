import React from "react";
import {shallow} from 'enzyme';
import LaunchSunriseEhrButton from "../../../src/components/admin/LaunchSunriseEhrButton";
import {expect} from '../../';

describe('LaunchSunriseEhrButton', () => {

  it('renders correctly', () => {
    const wrapper = shallow(<LaunchSunriseEhrButton loading={true}/>);
    expect(wrapper.find(Provider).exists());
    expect(wrapper.find("a").find(".button-sunrise-ehr-text"));
  });
});
