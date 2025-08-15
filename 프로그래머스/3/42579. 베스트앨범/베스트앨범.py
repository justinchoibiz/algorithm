def solution(genres, plays):
    answer = [];
    
    # {genre: total_play}
    genre_total_play = {};
    # {genere: [(play, id), ...]}
    genre_play_id = {};
    
    for idx, genre in enumerate(genres):
        play = plays[idx];
        
        genre_total_play[genre] = genre_total_play.get(genre, 0) + play;
        
        if genre not in genre_play_id:
            genre_play_id[genre] = [];
        genre_play_id[genre].append((play, idx));
        
    # [(genere, total_play), ...]
    sorted_genere = sorted(genre_total_play.items(), key = lambda x: -x[1])
    
    for genre, total_play in sorted_genere:
        
        # [(play, id), ...]
        sorted_songs_by_genre = sorted(genre_play_id[genre], key = lambda x: ( -x[0], x[1]))
        for play, id in sorted_songs_by_genre[:2]:
            answer.append(id);
    return answer;
        