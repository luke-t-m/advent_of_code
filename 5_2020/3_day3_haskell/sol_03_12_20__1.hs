import System.IO

treef _ _ [] = []
treef n r a@(l:ls) | n >= length l = treef (n - length l) r a
                   | otherwise = l!!n : treef (n+r) r ls

nT r d x = length (filter (\y -> y == '#') (treef 0 r (everyNth d x)))
 where
  everyNth _ [] = []
  everyNth d (x:xs) = x : everyNth d (drop (d-1) xs)

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 putStr "\npart 1: "
 print (nT 3 1 x)
 putStr "\npart 2: "
 print ((nT 1 1 x)
       *(nT 3 1 x)
       *(nT 5 1 x)
       *(nT 7 1 x)
       *(nT 1 2 x))
