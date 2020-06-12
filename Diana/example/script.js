const emojis = [
  {
    unicode: '&#1F490;',
    emoji: '💐'
  },
  {
    unicode: '&#1F33A;',
    emoji: '🌺'
  },
  {
    unicode: '&#1F33C;',
    emoji: '🌼'
  }
];

const holidayEmojis = [
  {
    emoji: '🎄',
    holiday: '3-17',
    countries: 'USA'
  },
  {
    emoji: '🍀',
    holiday: '12-25',
    countries: 'USA'
  },
  {
    emoji: '🎁',
    holiday: '5-28',
    countries: 'USA'
  }
];

const randomEmoji = () => {
  const randNum = Math.round(Math.random() * (emojis.length-1));
  return emojis[randNum].emoji;
};

const isHoliday = () => {
  const holidays = holidayEmojis.map((emoji) => emoji.holiday);
  const today = new Date();
  const monthDay = `${today.getMonth()+1}-${today.getDate()}`;
  return holidays.indexOf(monthDay);
};

const setEmoji = () => {
  let holiday = isHoliday();
  if(holiday > -1){
     document.getElementById('emoji_icon').innerHTML = holidayEmojis[holiday].emoji;
  }else{  
    document.getElementById('emoji_icon').innerHTML = randomEmoji();
  }
};

setEmoji();