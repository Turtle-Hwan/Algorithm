const playlist = [
    // {
    //     id: 0,
    //     genre: "classic",
    //     play: 500
    // }
]

const playCount = {
    // "classic" : 5000,
}

function solution(genres, plays) {
    genres.forEach((genre, i) => {
        playlist.push({
            "id": i,
            "genre": genre,
            "play": plays[i]
        });
        
        playCount[genre] ? playCount[genre] += plays[i] : playCount[genre] = plays[i];
    })
    
    console.log(playlist, playCount);
    
    const sortedGenres = Object.keys(playCount).sort(
        (a, b) => playCount[b] - playCount[a]);
    
    
    const answer = sortedGenres.map((genre) => {
        const playlist_filter = playlist.filter((music, i) => music.genre === genre);
        
        const sorted_playlist = playlist_filter.sort((a, b) => b.play - a.play === 0 ? a.id - b.id : b.play - a.play);
        
        return sorted_playlist.slice(0, 2).map((m) => m.id);
    })
    
    console.log(answer.flat());
    
    return answer.flat();
}