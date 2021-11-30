import System.IO



main :: IO ()
main = do
 inputs <- readFile "input.txt"
 let x = lines inputs
 print x 
