import Data.List
import Data.List.Unique
import Data.List.Split
import Data.Maybe


snds :: [(String,Int)] -> [(Int,String)]
snds x = map (\y -> (snd y, fst y)) x

shares :: Int -> String -> [(String,Int)] -> Int -> Bool
shares l x k n = lookup n (snds k) /= Nothing && length (repeated (x ++ (fromJust (lookup n (snds k))))) == l


conv :: [String] -> [(String,Int)] -> [(String,Int)]
conv ["|"] k = k
conv (x:xs) k  | length x == 6 && shares 2 x k 1 && shares 3 x k 4 = conv xs ((x,0):k)
               | length x == 2                                     = conv xs ((x,1):k)
               | length x == 5 && shares 2 x k 4                   = conv xs ((x,2):k)
               | length x == 5 && shares 4 x k 2                   = conv xs ((x,3):k)
               | length x == 4                                     = conv xs ((x,4):k)
               | length x == 5 && shares 4 x k 3                   = conv xs ((x,5):k)
               | length x == 6 && shares 5 x k 5 && shares 1 x k 1 = conv xs ((x,6):k)
               | length x == 3                                     = conv xs ((x,7):k)
               | length x == 7                                     = conv xs ((x,8):k)
               | length x == 6 && shares 5 x k 6 && shares 4 x k 4 = conv xs ((x,9):k)
               | otherwise = conv (xs++[x]) k

decode x = map (\y -> fromJust (lookup y (conv x []))) (last (splitOn ["|"] x))


main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = (map (filter (/="") . splitOn " ") (lines input))
 print (sum (map (length . (\y -> filter (\z -> (length z) `elem` [2,3,4,7]) (last (splitOn ["|"] y)))) x)) -- part 1
 print (sum (map (read . concat . map show . decode) x)) -- part 2
 print "done."
