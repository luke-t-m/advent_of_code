import System.IO
import Data.List.Split

makeVerts x | length (head x) == 1 = [map head x]
            | otherwise = map head x : makeVerts (map tail x) 

winIn (c:cs) m b | [] `elem` b = m
                 | otherwise = winIn cs (m+1) (map (filter (/=c)) b)


main :: IO ()
main = do
 doer minimum -- part 1
 doer maximum -- part 2


doer f = do
 input <- readFile "input.txt"
 let boards = tail (map (filter (/=[]) . map (filter (/="") . splitOn " ") . splitOn "\n") (splitOn "\n\n" input))
 let called = splitOn "," (head (lines input))
 let bboards = [ y ++ (makeVerts y) | y <- boards ]
 let winner = f (zip (map (winIn called 0) bboards) boards)
 let wcalls = fst (splitAt (fst winner) called)
 print (sum [read un | un <- concat (snd winner), not (un `elem` wcalls) ] * read (called!!(fst winner -1)))
