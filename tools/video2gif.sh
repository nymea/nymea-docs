echo "Make sure ffmpeg and gifsicle are installed"

if [ "$1" == "" ]; then
  echo "usage: $0 <videofile>"
  exit 1
fi

if [ ! -e "$1" ]; then
  echo "Input file does not exist"
  exit 1
fi

inputfile=$1
baseName=${inputfile%.*}
extension="${inputfile##*.}"
unoptimizedfile="$baseName"-unoptimized.gif
outputfile="$baseName".gif

echo "Working on $inputfile and rendering to $outputfile"

ffmpeg -i $inputfile -filter_complex "[0:v] palettegen" palette.png
ffmpeg -i $inputfile -i palette.png -filter_complex "[0:v][1:v] paletteuse" $unoptimizedfile
gifsicle $unoptimizedfile --optimize=10 --resize-width=1024 -o $outputfile

rm $unoptimizedfile palette.png
