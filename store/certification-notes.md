# Notes for certification (Partner Center › Submission › Notes for certification)

Paste the English block below. It explains the one feature a reviewer might ask about (the torrent client).

---

Hisn (iHisn) is a web browser (Chromium-based, Electron). No account or sign-in is needed to test it.

**BitTorrent client (Downloads › Torrents).** Hisn includes a built-in BitTorrent client for downloading and sharing legally distributable files (open-source software, public-domain and Creative Commons media, a user's own files). To be clear about what it is and is not:
- It does not search for, list, index or recommend any content, and it contains no built-in tracker, site list, links or catalogue. The user supplies a magnet link or a .torrent file they already have.
- Before the first use it shows a notice (in Arabic and English) that downloading or sharing copyrighted content without the owner's permission is the user's responsibility, and that other peers can see the user's IP address.
- Before downloading, it inspects the torrent's file list and warns about files that are likely to be harmful (programs, scripts, shortcuts, and files whose names are disguised, such as "film.mp4.exe").
- Sharing is off by default after a download finishes ("stop seeding"); the user can set download/upload speed limits.
- It uses ordinary BitTorrent connections (peers found through the trackers in the user's own magnet/.torrent and the public DHT, like any client). WebRTC is removed, and automatic router port-mapping (UPnP/NAT-PMP) and local-network discovery are off.
- The client runs in a separate process and saves to the user's Downloads folder (or a folder the user picks).

Copyright concerns can be reported to info@iegy.net and we act on them promptly (Policy 11.2).

The package is the Store edition: no self-updater (the Store updates it) and no video-download component. How to find the feature: open the ⋮ menu › Downloads (or press Ctrl+J), then the "Torrents" tab.

Privacy policy: https://iegy.net/H/privacy.html
