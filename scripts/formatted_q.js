const QUESTIONS = [
  {
    id: '14A',
    display_id: 14,
    dir: 'across',
    x: 6,
    y: 12,
    len: 14,
    ans: "AUTHENTICATION",
    code: `// System module AUTHENTICATION check\nfunction execute_authentication() {\n  return activate_protocol('6');\n}`,
    hint: "A process used to verify a user's identity, important in Zero Trust models used by Dell."
},
  {
    id: '11D',
    display_id: 11,
    dir: 'down',
    x: 10,
    y: 8,
    len: 13,
    ans: "VULNERABILITY",
    code: `// System module VULNERABILITY check\nfunction execute_vulnerability() {\n  return activate_protocol('8');\n}`,
    hint: "A flaw or weakness in a system that could be exploited."
},
  {
    id: '16D',
    display_id: 16,
    dir: 'down',
    x: 13,
    y: 12,
    len: 13,
    ans: "INSIDERTHREAT",
    code: `// System module INSIDERTHREAT check\nfunction execute_insiderthreat() {\n  return activate_protocol('5');\n}`,
    hint: "A cybersecurity risk that originates from within an organization."
},
  {
    id: '2D',
    display_id: 2,
    dir: 'down',
    x: 16,
    y: 1,
    len: 13,
    ans: "CYBERSECURITY",
    code: `// System module CYBERSECURITY check\nfunction execute_cybersecurity() {\n  return activate_protocol('3');\n}`,
    hint: "The protection of digital information and systems, a key focus area for Dell Technologies."
},
  {
    id: '15D',
    display_id: 15,
    dir: 'down',
    x: 8,
    y: 12,
    len: 11,
    ans: "THREATACTOR",
    code: `// System module THREATACTOR check\nfunction execute_threatactor() {\n  return activate_protocol('15');\n}`,
    hint: "An individual, group, or organization that conducts or intends to conduct harmful cyber activities."
},
  {
    id: '5D',
    display_id: 5,
    dir: 'down',
    x: 19,
    y: 3,
    len: 10,
    ans: "ENCRYPTION",
    code: `// System module ENCRYPTION check\nfunction execute_encryption() {\n  return activate_protocol('23');\n}`,
    hint: "Converting data into a form that cannot be easily understood by unauthorized users, widely used in Dell's security solutions."
},
  {
    id: '22A',
    display_id: 22,
    dir: 'across',
    x: 13,
    y: 18,
    len: 10,
    ans: "RANSOMWARE",
    code: `// System module RANSOMWARE check\nfunction execute_ransomware() {\n  return activate_protocol('9');\n}`,
    hint: "Malware that denies access to data until a ransom is paid, which Dell's recovery solutions help handle."
},
  {
    id: '13D',
    display_id: 13,
    dir: 'down',
    x: 6,
    y: 11,
    len: 10,
    ans: "DATABREACH",
    code: `// System module DATABREACH check\nfunction execute_databreach() {\n  return activate_protocol('20');\n}`,
    hint: "The unauthorized movement or disclosure of sensitive information, something companies like Dell Technologies work to prevent."
},
  {
    id: '10A',
    display_id: 10,
    dir: 'across',
    x: 6,
    y: 8,
    len: 9,
    ans: "ANTIVIRUS",
    code: `// System module ANTIVIRUS check\nfunction execute_antivirus() {\n  return activate_protocol('12');\n}`,
    hint: "Computer programs that can block, detect, and remove viruses and other malware."
},
  {
    id: '21D',
    display_id: 21,
    dir: 'down',
    x: 21,
    y: 16,
    len: 8,
    ans: "FIREWALL",
    code: `// System module FIREWALL check\nfunction execute_firewall() {\n  return activate_protocol('11');\n}`,
    hint: "Software designed to block unauthorized access to a network."
},
  {
    id: '20D',
    display_id: 20,
    dir: 'down',
    x: 17,
    y: 16,
    len: 8,
    ans: "SPOOFING",
    code: `// System module SPOOFING check\nfunction execute_spoofing() {\n  return activate_protocol('4');\n}`,
    hint: "Faking the sending address of a transmission to gain illegal access."
},
  {
    id: '18D',
    display_id: 18,
    dir: 'down',
    x: 19,
    y: 14,
    len: 8,
    ans: "PASSWORD",
    code: `// System module PASSWORD check\nfunction execute_password() {\n  return activate_protocol('7');\n}`,
    hint: "A string of characters used to authenticate an identity."
},
  {
    id: '3D',
    display_id: 3,
    dir: 'down',
    x: 7,
    y: 2,
    len: 8,
    ans: "PHISHING",
    code: `// System module PHISHING check\nfunction execute_phishing() {\n  return activate_protocol('19');\n}`,
    hint: "A method of tricking users into revealing sensitive information through fake messages or websites."
},
  {
    id: '9A',
    display_id: 9,
    dir: 'across',
    x: 4,
    y: 5,
    len: 7,
    ans: "PASSKEY",
    code: `// System module PASSKEY check\nfunction execute_passkey() {\n  return activate_protocol('14');\n}`,
    hint: "A modern, more secure alternative to passwords for user authentication."
},
  {
    id: '23A',
    display_id: 23,
    dir: 'across',
    x: 9,
    y: 23,
    len: 7,
    ans: "PRIVACY",
    code: `// System module PRIVACY check\nfunction execute_privacy() {\n  return activate_protocol('21');\n}`,
    hint: "The ability of individuals to control how their personal information is used."
},
  {
    id: '4D',
    display_id: 4,
    dir: 'down',
    x: 14,
    y: 2,
    len: 7,
    ans: "BACKUPS",
    code: `// System module BACKUPS check\nfunction execute_backups() {\n  return activate_protocol('2');\n}`,
    hint: "Extra copies of computer files that can be used to restore lost or damaged data."
},
  {
    id: '12A',
    display_id: 12,
    dir: 'across',
    x: 8,
    y: 10,
    len: 7,
    ans: "MALWARE",
    code: `// System module MALWARE check\nfunction execute_malware() {\n  return activate_protocol('10');\n}`,
    hint: "Software that disrupts or damages systems by performing unauthorized actions."
},
  {
    id: '1D',
    display_id: 1,
    dir: 'down',
    x: 9,
    y: 0,
    len: 7,
    ans: "DARKWEB",
    code: `// System module DARKWEB check\nfunction execute_darkweb() {\n  return activate_protocol('16');\n}`,
    hint: "Part of the internet that isn't indexed by search engines."
},
  {
    id: '7D',
    display_id: 7,
    dir: 'down',
    x: 4,
    y: 4,
    len: 7,
    ans: "SPYWARE",
    code: `// System module SPYWARE check\nfunction execute_spyware() {\n  return activate_protocol('22');\n}`,
    hint: "Software that is secretly installed into an information system without user knowledge."
},
  {
    id: '19D',
    display_id: 19,
    dir: 'down',
    x: 15,
    y: 15,
    len: 6,
    ans: "BOTNET",
    code: `// System module BOTNET check\nfunction execute_botnet() {\n  return activate_protocol('2');\n}`,
    hint: "A collection of computers compromised and controlled across a network."
},
  {
    id: '8A',
    display_id: 8,
    dir: 'across',
    x: 12,
    y: 4,
    len: 6,
    ans: "HACKER",
    code: `// System module HACKER check\nfunction execute_hacker() {\n  return activate_protocol('18');\n}`,
    hint: "An unauthorized user attempting to gain access to a system."
},
  {
    id: '6A',
    display_id: 6,
    dir: 'across',
    x: 0,
    y: 4,
    len: 5,
    ans: "VIRUS",
    code: `// System module VIRUS check\nfunction execute_virus() {\n  return activate_protocol('13');\n}`,
    hint: "A program that can replicate itself and spread harm."
},
  {
    id: '17A',
    display_id: 17,
    dir: 'across',
    x: 18,
    y: 14,
    len: 4,
    ans: "SPAM",
    code: `// System module SPAM check\nfunction execute_spam() {\n  return activate_protocol('17');\n}`,
    hint: "Unsolicited emails sent to many addresses."
},
  {
    id: '6D',
    display_id: 6,
    dir: 'down',
    x: 0,
    y: 4,
    len: 3,
    ans: "VPN",
    code: `// System module VPN check\nfunction execute_vpn() {\n  return activate_protocol('1');\n}`,
    hint: "A mechanism for creating a secure connection between a device and a network."
}
];

// grid cols: 23, grid rows: 25
