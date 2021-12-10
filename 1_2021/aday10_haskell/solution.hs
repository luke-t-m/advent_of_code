import Data.List
import Data.List.Split
import Data.Maybe

partners = [('(',')'),('[',']'),('{','}'),('<','>')]
scores = [(')',3),(']',57),('}',1197),('>',25137)]
scores2 = [(')',1),(']',2),('}',3),('>',4)]

scorer2 x = foldl op 0 (map (\t -> fromJust (lookup t scores2)) x)
 where op x = (+) (5 * x)

score w [] = 0
score w (x:xs) | length w /= 0 && x == head w = score (tail w) xs
               | x `elem` "([{<" = score ((fromJust (lookup x partners)) : w) xs
               | otherwise = fromJust (lookup x scores)

tocomplete w [] = w
tocomplete w (x:xs) | length w /= 0 && x == head w = tocomplete (tail w) xs
                    | x `elem` "([{<" = tocomplete ((fromJust (lookup x partners)) : w) xs

median x = head (snd (splitAt (((length x)-1) `div` 2) (sort x)))

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (sum (map (score []) x)) -- part 1
 let completable = filter (\t -> score [] t == 0) x
 print (median (map (scorer2 . tocomplete []) completable)) -- part 2
 print "done."
