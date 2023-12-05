type GiftWrapper<TPresent, TFrom, TTo> = {
  present: TPresent;
  from: TFrom;
  to: TTo;
};

const a: GiftWrapper<string, string, string> = {
  present: 'Car',
  from: 'Dan',
  to: 'Prime',
};
