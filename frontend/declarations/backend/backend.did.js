export const idlFactory = ({ IDL }) => {
  return IDL.Service({
    'addImageUrl' : IDL.Func([IDL.Text], [], []),
    'getAllImageUrls' : IDL.Func([], [IDL.Vec(IDL.Text)], ['query']),
    'getRandomImageUrl' : IDL.Func([], [IDL.Text], []),
  });
};
export const init = ({ IDL }) => { return []; };
