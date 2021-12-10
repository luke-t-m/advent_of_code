import Data.List
import Data.List.Split
import Data.Maybe

partners = [('(',')'),('[',']'),('{','}'),('<','>')]
scores = [(')',3),(']',57),('}',1197),('>',25137)]
scores2 = [(')',1),(']',2),('}',3),('>',4)]

op x = (+) (5 * x)

scorer2 x = foldl op 0 (map (\t -> fromJust (lookup t scores2)) x)


score w [] = 0
score w (x:xs) | length w /= 0 && x == head w = score (tail w) xs
               | x `elem` "([{<" = score ((fromJust (lookup x partners)) : w) xs
               | otherwise = fromJust (lookup x scores)

tocomplete w [] = w
tocomplete w (x:xs) | length w /= 0 && x == head w = tocomplete (tail w) xs
                    | x `elem` "([{<" = tocomplete ((fromJust (lookup x partners)) : w) xs

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (sum (map (score []) x)) -- part 1
 let completable = filter (\t -> score [] t == 0) x
 print (head $ snd (splitAt (((length completable)-1) `div` 2) (sort (map (scorer2 . tocomplete []) (completable))))) -- part 2
 print "done."
