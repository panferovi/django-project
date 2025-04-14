        let stats = {
            correct: 0,
            wrong: 0,
            topics: {
                addition: { total: 0, correct: 0 },
                subtraction: { total: 0, correct: 0 },
                comparison: { total: 0, correct: 0 },
                logic: { total: 0, correct: 0 },
                geometry: { total: 0, correct: 0 },
                time: { total: 0, correct: 0 },
                money: { total: 0, correct: 0 }
            }
        };
        function updateStats() {
            document.getElementById('correctCount').textContent = stats.correct;
            document.getElementById('wrongCount').textContent = stats.wrong;
            
            let progressHTML = '';
            for (const [topic, data] of Object.entries(stats.topics)) {
                if (data.total > 0) {
                    const percent = Math.round((data.correct / data.total) * 100);
                    progressHTML += `
                        <div class="mb-2">
                            <div class="d-flex justify-content-between">
                                <span>${topicName(topic)}</span>
                                <span>${percent}%</span>
                            </div>
                            <div class="progress" style="height: 20px;">
                                <div class="progress-bar" style="width: ${percent}%"></div>
                            </div>
                        </div>
                    `;
                }
            }
            document.getElementById('topicProgress').innerHTML = progressHTML;
        }
