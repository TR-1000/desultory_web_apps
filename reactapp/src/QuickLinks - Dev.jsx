import React, { useState, Fragment } from 'react';
import AutoDialerModal from 'app/AutoDialer/v1/components/modals/AutoDialerModal';
import { I18n, translateMarkupString } from '@td/shared_utils';
import { MODAL_TYPES } from 'app/AutoDialer/v1/constants/modal-types';

import './quick-links.scss';

const QuickLinks = providerData => {
  const [modalType, setModalType] = useState('');
  const handleClose = () => setModalType('');
  const specialty = providerData.serviceSpecialty;
  const shouldRenderAutodialer =
    specialty ===
    (('General Medical' && Boolean(window.FEATURE_TOGGLES.allow_auto_dialer)) ||
      ('Nutrition' && Boolean(window.FEATURE_TOGGLES.nut_allow_auto_dialer)) ||
      ('Mental Health' && Boolean(window.FEATURE_TOGGLES.mh_allow_auto_dialer)));

  return (
    <section className="module quick-links">
      <h1>Quick Links</h1>
      <ul className="list with_arrows">
        <li>
          <a href="https://www.teladoc.com/provider-resources/" rel="noopener noreferrer" target="_blank">
            Provider Resources
          </a>
        </li>
        {specialty === 'General Medical' && (
          <li>
            <a
              href="https://www.teladoc.com/provider-resources/covid-19-protocol-and-guidance/"
              rel="noopener noreferrer"
              target="_blank"
            >
              Covid-19 Guidelines
            </a>
          </li>
        )}
        <li>
          <a
            href="https://s3.amazonaws.com/communications.teladoc.com/resources/video_support/Provider_Video_FAQ_Document.pdf"
            rel="noopener noreferrer"
            target="_blank"
          >
            Video FAQ
          </a>
        </li>
        <li>
          <a
            href="/test_video"
            id="video-test"
            rel="noopener noreferrer"
            target="_blank"
            title="Test Video Capabilities"
          >
            Test Video Capabilities
          </a>
        </li>
        {shouldRenderAutodialer && (
          <Fragment>
            <li>
              <span
                className="quick-link"
                title="Test Audio Capabilities"
                id="audio-test-link"
                onClick={() => setModalType(MODAL_TYPES.AUDIO_TEST)}
              >
                Test Audio Capabilities
              </span>
            </li>
            <li>
              <span className="auto-dialer-link" id="audio-faq-link">
                <a
                  href="https://s3.amazonaws.com/communications.teladoc.com/resources/video_support/Provider_Audio_FAQ_Document.pdf"
                  rel="noopener noreferrer"
                  target="_blank"
                >
                  <I18n scope="autodialer.call_interface.footer" text="faq" />
                </a>
              </span>
            </li>
          </Fragment>
        )}
      </ul>
      <AutoDialerModal handleClose={handleClose} modalType={modalType} />
    </section>
  );
};

export default QuickLinks;
