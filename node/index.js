require('dotenv').config();
const fs = require('fs');

const fetchWallpapers = async () => {
  const wallpapersURL = `${process.env.BASE_URL}${process.env.USERNAME}/${process.env.COLLECTION_ID}?apikey=${process.env.API_KEY}`;
  const res = await fetch(wallpapersURL);
  const { data } = await res.json();

  let wallpapers = [];

  data.map((wallpaper) => {
    wallpapers.push({ url: wallpaper.path });
  });

  fs.writeFile(
    'wallpapers.json',
    JSON.stringify(wallpapers, null, 2),
    'utf-8',
    (err) => {
      if (err) throw err;
    }
  );
};

const wallpapers = fetchWallpapers();
